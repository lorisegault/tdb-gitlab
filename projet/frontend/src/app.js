function apiFetch(path) {
  return fetch(`/api${path}`).then((r) => {
    if (!r.ok) throw new Error(r.statusText);
    return r.json();
  });
}

function showSection(id) {
  document.querySelectorAll(".section").forEach((s) => s.classList.add("hidden"));
  document.getElementById(id).classList.remove("hidden");
}
