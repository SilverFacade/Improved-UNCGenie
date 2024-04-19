import "./index.scss"
import { useState, useEffect } from "react";
import jpg1 from '../imgs/uncgEUC.jpg';
import Nav from '../Nav';

const ClassInfo = () => {
    const [courses, setCourses] = useState(null);

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
        console.log(title);
    
        document.getElementById('classTitle').innerHTML = title;
        document.getElementById('desc').innerHTML = description;
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
                    <h2>Description:</h2>
                </div>
                <div id ={'descDiv'}>
                    <p id={'desc'}></p>
                </div>
            </div>

            <div className={'classinfopics'}>
                <img id={'photo1'} src={jpg1} alt="Stock Photo" ></img>
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