import re
from pyvis.network import Network

def parse_jil(file_path):
    jobs = {}
    current_job = None

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("insert_job:"):
                if current_job:
                    jobs[current_job['name']] = current_job
                current_job = {'name': line.split()[1], 'condition': '', 'box_name': None}
            elif current_job:
                if line.startswith("box_name:"):
                    current_job['box_name'] = line.split()[1]
                elif line.startswith("condition:"):
                    current_job['condition'] = line[len("condition:"):].strip()

        if current_job:
            jobs[current_job['name']] = current_job

    return jobs

def extract_dependencies(jobs):
    edges = []
    for job in jobs.values():
        cond = job.get('condition', '')
        if cond:
            # Extract job names inside success(...)
            dependencies = re.findall(r'success\(([\w\.]+)\)', cond)
            for dep in dependencies:
                edges.append((dep, job['name']))
    return edges

def mock_statuses(jobs):
    statuses = ['SU', 'FA', 'RU', 'IN']  # Success, Fail, Running, Inactive
    job_status = {}
    for i, job in enumerate(jobs):
        job_status[job] = statuses[i % len(statuses)]
    return job_status

def visualize_graph(jobs, edges, statuses):
    net = Network(height="700px", width="100%", directed=True)
    status_colors = {'SU': 'green', 'FA': 'red', 'RU': 'orange', 'IN': 'gray'}

    for job in jobs:
        color = status_colors.get(statuses.get(job, 'IN'), 'black')
        net.add_node(job, label=job, color=color, title=f"Status: {statuses.get(job, 'IN')}")

    for src, dst in edges:
        net.add_edge(src, dst)

    net.show("autosys_job_graph.html")
    print("Graph saved as autosys_job_graph.html — open this in your browser.")

if __name__ == "__main__":
    jil_file = "autosys_jobs.jil"  # your JIL file here
    jobs = parse_jil(jil_file)
    edges = extract_dependencies(jobs)
    statuses = mock_statuses(jobs)
    visualize_graph(jobs, edges, statuses)
