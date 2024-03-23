import "./index.scss"
import {useState, useEffect} from "react";
import Nav from '../Nav';

const Home = () => {
    const [registered, setRegistered] = useState(null);
    const [student, setStudent] = useState(null);

    async function getRegistered(e){
        if(registered) {
            setRegistered(null);
            return;
        }

        fetch('/api/sectionsRegistered', 
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
                    {student && <h1 id={'welcome'}>Welcome, {student[0].first_name}</h1>}
                    
                    
                    <p>Plan your schedule, register, Look for information on courses, etc...</p>
                    
                    <div id={'redirectButtons'}>
                        <a href="/register">
                            <button type = "button" id={'registerButton'}> Register!</button>
                        </a>
                        <a href="/classInfo">
                            <button type = "button" id={'classInfoButton'}>Course Info</button>
                        </a>
                    </div>


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

                    <div id={'degreeprogress'}>
                        <button type = "button" id={'degree-progress-button'}>View Progress</button>
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

                </div>
            </>
        )
    } else {    
        return (
            <>
                <Nav/>
                <div id={'generalHomepage'}>
                   <p>General Homepage here</p>
                </div>
            </>
        )
    }
}

export default Home