import { useState } from "react";

const BASE_URL = "https://ethara-fullstack-app-production.up.railway.app";

export default function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [project, setProject] = useState("");
  const [desc, setDesc] = useState("");

  const [task, setTask] = useState("");

  const [dashboard, setDashboard] = useState(null);

  const signup = async () => {
    const res = await fetch(`${BASE_URL}/signup?email=${email}&password=${password}`, { method: "POST" });
    const data = await res.json();
    alert(JSON.stringify(data));
  };

  const login = async () => {
    const res = await fetch(`${BASE_URL}/login?email=${email}&password=${password}`, { method: "POST" });
    const data = await res.json();
    alert(JSON.stringify(data));
  };

  const createProject = async () => {
    const res = await fetch(`${BASE_URL}/projects?name=${project}&description=${desc}`, { method: "POST" });
    const data = await res.json();
    alert(JSON.stringify(data));
  };

  const createTask = async () => {
    const res = await fetch(`${BASE_URL}/tasks?title=${task}&description=work&project_id=1&assigned_to=1`, { method: "POST" });
    const data = await res.json();
    alert(JSON.stringify(data));
  };

  const loadDashboard = async () => {
    const res = await fetch(`${BASE_URL}/dashboard`);
    const data = await res.json();
    setDashboard(data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Task Manager 🚀</h1>

      <h2>Signup</h2>
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={signup}>Signup</button>

      <h2>Login</h2>
      <button onClick={login}>Login</button>

      <h2>Create Project</h2>
      <input placeholder="Name" onChange={(e) => setProject(e.target.value)} />
      <input placeholder="Description" onChange={(e) => setDesc(e.target.value)} />
      <button onClick={createProject}>Create Project</button>

      <h2>Create Task</h2>
      <input placeholder="Task Title" onChange={(e) => setTask(e.target.value)} />
      <button onClick={createTask}>Create Task</button>

      <h2>Dashboard</h2>
      <button onClick={loadDashboard}>Load Dashboard</button>

      {dashboard && (
        <div>
          <p>Total: {dashboard.total_tasks}</p>
          <p>Done: {dashboard.completed_tasks}</p>
          <p>Pending: {dashboard.pending_tasks}</p>
        </div>
      )}
    </div>
  );
}