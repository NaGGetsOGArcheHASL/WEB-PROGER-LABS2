function fillCourseList() {
    console.log('fillCourseList called');
    fetch('/lab8/api/courses/')
    .then(function (data) {
        return data.json();
    })
    .then(function (courses) {
        let tbody = document.getElementById('course-list');
        tbody.innerHTML = '';
        for(let i = 0; i<courses.length; i++) {
            tr = document.createElement('tr');

            let tdName = document.createElement('td');
            tdName.innerText = courses[i].name;

            let tdVideos = document.createElement('td');
            tdVideos.innerText = courses[i].videos;

            let tdPrice = document.createElement('td');
            tdPrice.innerText = courses[i].price || 'бесплатно';

            let tdCreationDate = document.createElement('td');
            tdCreationDate.innerText = courses[i].creation_date;

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';
            editButton.onclick = function() {
                editCourse(i, courses[i]);
            };

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteCourse(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdCreationDate);
            tr.append(tdActions);
            tbody.append(tr);
        }
    })
}


function deleteCourse(num) {
    console.log('deleteCourse called');
    if(! confirm('Вы точно хотите удалить курс?')){
        return;
    }

    fetch(`/lab8/api/courses/${num}`, {method: 'DELETE'})
    .then(function() {
        fillCourseList();
    });
}


function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}


function cancel() {
    hideModal();
}


function addCourse() {
    document.getElementById('num').value = '';
    document.getElementById('name').value = '';
    document.getElementById('videos').value = '';
    document.getElementById('price').value = '';
    showModal();
}


function sendCourse() {
    console.log('sendCourse called');
    const num = document.getElementById('num').value;
    const course = {
        name: document.getElementById('name').value,
        videos: document.getElementById('videos').value,
        price: document.getElementById('price').value
    }

    const url = `/lab8/api/courses/${num}`;
    const method = num ? 'PUT' : 'POST';
    fetch(url, {
        method: method,
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(course)
    })
    .then(function() {
        fillCourseList();
        hideModal();
    })
}


function editCourse(num, course) {
    document.getElementById('num').value = num;
    document.getElementById('name').value = course.name;
    document.getElementById('videos').value = course.videos;
    document.getElementById('price').value = course.price;
    showModal();
}