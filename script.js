document.getElementById('gradeForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const grade = document.getElementById('grade').value;

    const response = await fetch('/add_student', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, grade: parseFloat(grade) })
    });

    if (response.ok) {
        loadStudents();
    }
});

async function loadStudents() {
    const res = await fetch('/get_students');
    const students = await res.json();

    const tableBody = document.getElementById('studentTable');
    tableBody.innerHTML = '';

    for (let [name, grade] of Object.entries(students)) {
        const row = `<tr><td>${name}</td><td>${grade}</td></tr>`;
        tableBody.innerHTML += row;
    }

    const avgRes = await fetch('/average_grade');
    const avgData = await avgRes.json();
    document.getElementById('averageGrade').textContent = avgData.average_grade || '-';
}

loadStudents();
