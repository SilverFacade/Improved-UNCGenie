import "./index.scss"
import {useState, useEffect} from "react";
import jpg1 from '../imgs/UNCGphoto.jpg';
import Nav from '../Nav';
import Login from '../Login';
import Progress from "../Progress";

const Home = () => {
    const [registered, setRegistered] = useState(null);
    const [student, setStudent] = useState(null);
    const [progress, setProgress] = useState(null);

    async function getRegistered(e){
        if(registered) {
            setRegistered(null);
            return;
        }

        fetch('/api/sections_registered', 
        {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setRegistered(data);
        });
    }   
    
    useEffect(() => {
        fetch('/api/student', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setStudent(data);
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

    const tasks = [];
    const [initState, setInit] = useState(tasks);
    function AddToList(e) {
        e.preventDefault();
        let input = document.getElementById('taskinput').value;
        setInit([...initState, input]);        //const Task =
        document.getElementById('taskinput').value = '';
    }

    
    if(localStorage.getItem('token')) {
        return ( 
            <>
            <Nav/>
                <div id={'mainDiv'}>
                    {student && <h1 id={'welcome'}>Welcome, {student[0].first_name}!</h1>}

                    <div id={'redirectButtons'}>
                        <a href="/register">
                            <button type = "button" id={'registerButton'}> Register</button>
                        </a>
                        <a href="/classInfo">
                            <button type = "button" id={'classInfoButton'}>Course Info</button>
                        </a>
                        <a href="/progress">
                            <button type = "button" id={'progressButton'}>Degree Progress</button>
                        </a>
                    </div>

                    <div className={'homepicture'}>
                        <img id={'photo1'} src={jpg1} alt="Stock Photo" ></img>
                    </div>

                    <div className={'homepictureDesc'}>
                        <h1>Web Registration App</h1>
                        <p>A new and intuitive app for class observation and registration. To start, check your
                            Degree Progress to see where you stand and what classes are you should plan to take 
                            this semester. Once you have an idea of what classes to take, check out information about
                            them. Finally, register for your classes!
                        </p>
                    </div>

                    <form className={'todo'} onSubmit={(e) => AddToList(e)} id={'todo'}>
                        <span>
                            {
                                initState.map((task) => (<div onClick={(e)=>e.target.remove()}> {task}</div>))
                            }
                        </span>
                        <input type={'text'} placeholder={'Enter Task Here'} id={'taskinput'} required/>
                        <input type={'submit'} value={'Add To List'}/>
                    </form>

                    <div id={'currentSchedule'}>
                        <button type = "button" id={'checkScheduleButton'} onClick={(e) => 
                        getRegistered(e)}>Check Schedule</button>
                            <table className = {'registered-classes-table'}>
                            {registered && <thead>
                                <tr className = {'registered-classes-table-column-headers'}>
                                    <th>Subject</th>
                                    <th>Course Number</th>
                                    <th>Section Number</th>     
                                    <th>Days</th>
                                    <th>Time</th>
                                </tr>
                            </thead>}
                            <tbody>
                                {registered && registered.map((regcourse, i) => (
                                <tr id = 'registered-classes-table-row' key={i}>
                                    <td>{regcourse.subject}</td>
                                    <td>{regcourse.course_number}</td>
                                    <td>{regcourse.section_number}</td>
                                    <td>{regcourse.days}</td>
                                    <td>{regcourse.start_time}-{regcourse.end_time}</td>
                                </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>

                    <h2 id={'degreeprogressheader'}>Degree Progress: {progress && progress.progress*100}%</h2>
                    <progress id={'degreeprogress'} value={progress && progress.progress*100} max="100"></progress>
                    
                </div>
            </>
        )
    } else {    
        return (
            <>
                <Login/>
            </>
        )
    }
}

export default Home