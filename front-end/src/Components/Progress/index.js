import "./index.scss"
import Nav from '../Nav';
import {useState, useEffect} from "react";

const Progress = () => {
    const [remaining, setRemaining] = useState(null);
    const [completed, setCompleted] = useState(null);
    const [progress, setProgress] = useState(null);

    useEffect(() => {
        fetch('/api/courses_remaining', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setRemaining(data);
        });

        fetch('/api/courses_completed', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setCompleted(data);
        });

        fetch('/api/graduation_progress', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setProgress(data);
        });
    }, []); 

    return (
        <>
            <Nav/>
            <div className={'remaining'} id={'remaining'}>
                <ul id = {'remainingList'}>
                    <h1>Remaining Classes</h1>
                    {remaining && remaining.map((course, i) => (
                        <li key={i}>{course.subject} {course.course_number}</li>
                    ))}
                </ul>
            </div>
            <div className={'completed'} id={'completed'}>
                <ul id = {'completedList'}>
                <h1>Completed Classes</h1>
                    {completed && completed.map((course, i) => (
                        <li key={i}>{course.subject} {course.course_number} Grade: {course.grade}</li>
                    ))}
                </ul>
            </div>

            <h2 id={'degreeprogressheader'}>Degree Progress: {progress && progress.progress*100}%</h2>
            <progress id={'degreeprogress'} value={progress && progress.progress*100} max="100"></progress>
        </>
    )
}

export default Progress