const PROJECT_ID = 1;

function apiFetch(path) {
  return fetch(`/api${path}`).then((r) => {
    if (!r.ok) throw new Error(r.statusText);
    return r.json();
  });
}

function showSection(id) {
  document.querySelectorAll(".section").forEach((s) => s.classList.add("hidden"));
  document.getElementById(id).classList.remove("hidden");
  document.querySelectorAll(".nav-btn").forEach((b) => b.classList.remove("active"));
  const btn = document.querySelector(`[data-section="${id}"]`);
  if (btn) btn.classList.add("active");
}

let currentSection = "home";

function renderApp() {
  document.getElementById("root").innerHTML = `
    <nav class="nav">
      <h1 class="nav-title">TDB GitLab</h1>
      <div class="nav-links">
        <button class="nav-btn active" data-section="home" onclick="navigate('home')">Accueil</button>
        <button class="nav-btn" data-section="pipelines" onclick="navigate('pipelines')">Pipelines</button>
        <button class="nav-btn" data-section="secrets" onclick="navigate('secrets')">Secrets</button>
      </div>
    </nav>
    <main id="content">
      <div id="home" class="section"></div>
      <div id="pipelines" class="section hidden"></div>
      <div id="secrets" class="section hidden"></div>
    </main>
  `;
  navigate("home");
  setInterval(poll, 3000);
}

function navigate(section) {
  currentSection = section;
  showSection(section);
  loadSection(section);
}

function loadSection(section) {
  const el = document.getElementById(section);
  el.innerHTML = `<div class="loading">Chargement...</div>`;
  if (section === "home") loadHome(el);
  else if (section === "pipelines") loadPipelines(el);
  else if (section === "secrets") loadSecrets(el);
}

function poll() {
  loadSection(currentSection);
}

async function loadHome(el) {
  try {
    const [repo, stats] = await Promise.all([
      apiFetch(`/repository/${PROJECT_ID}`),
      apiFetch(`/repository/${PROJECT_ID}/stats`),
    ]);
    el.innerHTML = `
      <h2 class="section-title">Dépôt</h2>
      <div class="card">
        <p><strong>Nom :</strong> ${repo.name}</p>
        <p><strong>Description :</strong> ${repo.description || "—"}</p>
        <p><strong>Branche :</strong> ${repo.default_branch}</p>
        <p><strong>Dernière activité :</strong> ${repo.last_activity_at || "—"}</p>
      </div>
      <div class="stats-row">
        <div class="stat-card">MRs ouvertes<br><span class="stat-value">${stats.open_merge_requests}</span></div>
        <div class="stat-card">Issues ouvertes<br><span class="stat-value">${stats.open_issues}</span></div>
        <div class="stat-card">Pipelines<br><span class="stat-value">${stats.pipelines}</span></div>
      </div>
      <button class="btn" onclick="syncRepo()">Synchroniser</button>
    `;
  } catch {
    el.innerHTML = `<div class="error">Erreur de chargement</div>`;
  }
}

async function syncRepo() {
  try {
    await apiFetch(`/repository/${PROJECT_ID}/sync`, { method: "POST" });
    loadSection("home");
  } catch {
    alert("Erreur de synchronisation");
  }
}

async function loadPipelines(el) {
  try {
    const data = await apiFetch(`/pipelines/${PROJECT_ID}`);
    el.innerHTML = `
      <h2 class="section-title">Pipelines</h2>
      <button class="btn" onclick="syncPipelines()">Synchroniser</button>
      <table class="table">
        <thead><tr><th>Statut</th><th>Branche</th><th>Durée</th><th>Date</th></tr></thead>
        <tbody>
          ${data.map((p) => `
            <tr>
              <td><span class="badge badge-${p.status}">${p.status}</span></td>
              <td>${p.branch}</td>
              <td>${p.duration ? p.duration + "s" : "—"}</td>
              <td>${p.created_at || "—"}</td>
            </tr>
          `).join("")}
        </tbody>
      </table>
    `;
  } catch {
    el.innerHTML = `<div class="error">Erreur de chargement</div>`;
  }
}

async function syncPipelines() {
  try {
    await apiFetch(`/pipelines/${PROJECT_ID}/sync`, { method: "POST" });
    loadSection("pipelines");
  } catch {
    alert("Erreur de synchronisation");
  }
}

async function loadSecrets(el) {
  try {
    const data = await apiFetch(`/secrets/${PROJECT_ID}`);
    el.innerHTML = `
      <h2 class="section-title">Secrets</h2>
      <table class="table">
        <thead><tr><th>Nom</th><th>Valeur</th></tr></thead>
        <tbody>
          ${data.variables.map((v) => `
            <tr><td>${v.key}</td><td>••••••••</td></tr>
          `).join("")}
        </tbody>
      </table>
    `;
  } catch {
    el.innerHTML = `<div class="error">Erreur de chargement</div>`;
  }
}

document.addEventListener("DOMContentLoaded", renderApp);
