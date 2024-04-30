import "./index.scss"
import { useState, useEffect } from "react";
import Nav from '../Nav';

const ClassInfo = () => {
    const [courses, setCourses] = useState(null);
    const [reqs, setReqs] = useState(null);
    const [subjects, setSubjects] = useState(null);

    useEffect(() => {
        fetch('/api/subjects', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setSubjects(data);
        });
    }, []); 

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

            document.getElementById('classTitleTitle').innerHTML = "Course:";
            document.getElementById('descTitle').innerHTML = "Description:";
            document.getElementById('creditsTitle').innerHTML = "Credits:";
            document.getElementById('requisitesTitle').innerHTML = "Prerequisites:";

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
                    <option>Select...</option>
                        {subjects && subjects.map((subject, i) => (
                        <option key={i} value ={subject.subject}>
                            {subject.subject}
                        </option>
                    ))}
                </select>
            </div>

            <div id = {'scrollList'}>
                <nav>
                    <ul id = {'classList'}>
                        {courses && courses.map((course, i) => (
                            <li key={i} onClick={(e) => 
                                renderClassInfo(e, course.subject, course.course_number, course.credits, course.title, course.description)}>
                                {course.subject} {course.course_number} : {course.title}
                            </li>
                        ))}
                    </ul>
                </nav>
            </div>

            <div className = {'classInfoDiv'}>
                <div id ={'titleDiv'}>
                    <h1 id={'classTitleTitle'}></h1>
                    <p id={'classTitle'}>This is the Class Information Page. Select a subject and course
                    on the left to view information about that course.</p>
                </div>
                <div id ={'descDiv'}>
                    <h2 id={'descTitle'}></h2>
                    <p id={'desc'}></p>
                    <h2 id={'creditsTitle'}></h2>
                    <p id={'credits'}></p>
                    <h2 id={'requisitesTitle'}></h2>
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