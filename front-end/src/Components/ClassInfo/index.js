import "./index.scss"
import { useState, useEffect } from "react";
import Nav from '../Nav';

const ClassInfo = () => {
    const [courses, setCourses] = useState(null);

    useEffect(() => {
        fetch('/api/courses', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setCourses(data);
        });
    }, []);


    async function renderClassInfo(e, subject, course_number, credits, title, description) {  
        console.log(title);
    
        document.getElementById('classTitle').innerHTML = title;
        document.getElementById('desc').innerHTML = description;
    }

    if(localStorage.getItem('token')) {
        return (
            <>
            <Nav/>
            <div className = {'scrollList'}>
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