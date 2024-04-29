import "./index.scss"
import { useState, useEffect } from "react";
import Nav from '../Nav';

const ClassInfo = () => {
    const [courses, setCourses] = useState(null);
    const [reqs, setReqs] = useState(null);


    async function getClasses(e){
        let sub = document.querySelector('#subjectDropdown');
        sub = sub.value;

        fetch('/api/courses', 
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token'),
                "subject": sub
            }
        }).then(res=> {
            return res.json();
        }).then(data => {
            setCourses(data);
        });
    }

    async function renderClassInfo(e, subject, course_number, credits, title, description) {  
        fetch('/api/course_reqs', 
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token'),
                "subject": subject,
                "courseNum": course_number
            }
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setReqs(data);

            if (data[2]) {
                document.getElementById('requisites').innerHTML = data[0].req_course_subject + " " + data[0].req_course_number
                    + ", " + data[1].req_course_subject + " " + data[1].req_course_number + ", " + data[2].req_course_subject + " " + data[2].req_course_number;
            } else if (data[1]) {
                document.getElementById('requisites').innerHTML = data[0].req_course_subject + " " + data[0].req_course_number
                + ", " + data[1].req_course_subject + " " + data[1].req_course_number;
            } else if (data[0]) {
                document.getElementById('requisites').innerHTML = data[0].req_course_subject + " " + data[0].req_course_number;
            } else {
                document.getElementById('requisites').innerHTML = "None";
            }
        });
    
        document.getElementById('classTitle').innerHTML = subject + " " + course_number + ":\n" + title;
        document.getElementById('desc').innerHTML = description;
        document.getElementById('credits').innerHTML = credits; 
    }

    if(localStorage.getItem('token')) {
        return (
            <>
            <Nav/>
            <div id ={'selectSubject'}>
                <select id= {'subjectDropdown'} onChange={(e) => getClasses(this)}>
                    <option value="">Select...</option>
                    <option value="CSC">CSC</option>
                    <option value="MAT">MAT</option>
                    <option value="PHI">PHI</option>
                    <option value="HIS">HIS</option>
                    <option value="BIO">BIO</option>
                    <option value="PHY">PHY</option>
                </select>
            </div>

            <div id = {'scrollList'}>
                <nav>
                    <ul id = {'classList'}>
                        {courses && courses.map((course, i) => (
                            <li key={i} onClick={(e) => 
                                renderClassInfo(e, course.subject, course.course_number, course.credits, course.title, course.description)}>
                                {course.title}
                            </li>
                        ))}
                    </ul>
                </nav>
            </div>

            <div className = {'classInfoDiv'}>
                <div id ={'titleDiv'}>
                    <h1>Course:</h1>
                    <p id={'classTitle'}></p>
                </div>
                <div id ={'descDiv'}>
                    <h2>Description:</h2>
                    <p id={'desc'}></p>
                    <h2>Credits:</h2>
                    <p id={'credits'}></p>
                    <h2>Prerequisites:</h2>
                    <p id={'requisites'}></p>
                </div>
            </div>
            </>
        )
    } else {    
        return (
            <div className={'loginRequired'}>
                <p>You must Login</p>
            </div>
        )
    }
}

export default ClassInfo