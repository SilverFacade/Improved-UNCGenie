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
    


    /*
    async function progress(e) {
        e.preventDefault();
        const user = document.querySelector('form [name="username"]');
        const pass = document.querySelector('form [name="password"]');
        const request = await fetch('/api/progress', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: user.value,
                password: pass.value
            }) // curls for defining json objects & params when talking about data types
        }).then((res) => res.json()); //it needs a json object as second variable
        if (request.status === 200) {
            localStorage.setItem('token', request.token); // Holds onto the data locally
            window.location.href = '/progress';
        } else alert(request.message); //later replace with modal (mode el)
    }

    const tasks = [];
    const [initState, setInit] = useState(tasks);
    function AddToList(e) {
        e.preventDefault();
        let input = document.getElementById('taskinput').value;
        setInit([...initState, input]);        //const Task =
        document.getElementById('taskinput').value = '';
    }
    */

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
                        <li key={i}>{course.subject} {course.course_number}</li>
                    ))}
                </ul>
            </div>

            <h2 id={'degreeprogressheader'}>Degree Progress: {progress && progress.progress*100}%</h2>
            <progress id={'degreeprogress'} value={progress && progress.progress*100} max="100"></progress>
        </>
    )
}

export default Progress