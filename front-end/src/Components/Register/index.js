import { useState } from "react";
import "./index.scss"

let displayRegTable = false;
let displaySchTable = false;

const Register = () => {
    const [sections, setSections] = useState(null);
    const [schedule, setSchedule] = useState(null);
    const [registered, setRegistered] = useState(null);
    
    async function getSections(e){
        var sub = document.querySelector('.subject-dropdown');
        var courseNum = document.querySelector('.course-number-dropdown');

        fetch('/api/sections', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token'),
                "subject": sub.value,
                "courseNumber": courseNum.value
            }            
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setSections(data);
        });
    }


    async function getCRDropdownValue(e){
        var dropDownValue = document.querySelector('.register-or-schedule-dropdown');

        if (dropDownValue.value === "registered-classes") {
            displayRegTable = true;
            displaySchTable = false;
            getRegistered(e);
        } else if (dropDownValue.value === "schedules") {
            displaySchTable = true;
            displayRegTable = false;
            getSchedule(e);
        }
    }


    async function getRegistered(e){
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


    async function getSchedule(e){
        fetch('/api/schedule', 
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
            setSchedule(data);
        });
    }


    async function registerFromScheduleTable(e){
        var sub = document.querySelector('#scheduleSub');
        var courseNum = document.querySelector('#scheduleCourseNum');
        var sectionNum = document.querySelector('#scheduleSection');

        fetch('/api/register', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub.textContent,
                courseNumber: courseNum.textContent,
                sectionNumber: sectionNum.textContent
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            // if the server returns an error key with json it means the request failed.
            if (data.error) {
                alert(data.error);
            } else{
                console.log(data);
                setRegistered(data); 
                getSchedule();
            }
        });
    }

    
    async function removeFromSchedule(e){
        var sub = document.querySelector('#subject');
        var courseNum = document.querySelector('#courseNum');
        var sectionNum = document.querySelector('#sectionNum');

        fetch('/api/removeFromSchedule', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub.textContent,
                courseNumber: courseNum.textContent,
                sectionNumber: sectionNum.textContent
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            console.log(data);
            setSchedule(data);
        });
    }


    async function registerFromRegisterTable(e){
        var sub = document.querySelector('#subject');
        var courseNum = document.querySelector('#courseNum');
        var sectionNum = document.querySelector('#sectionNum');   

        fetch('/api/register', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub.textContent,
                courseNumber: courseNum.textContent,
                sectionNumber: sectionNum.textContent
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            // if the server returns an error key with json it means the request failed.
            if (data.error) {
                alert(data.error);
            } else{
                console.log(data);  
                setRegistered(data);
            }
        });
    }


    async function addToSchedule(e){
        var sub = document.querySelector('#subject');
        var courseNum = document.querySelector('#courseNum');
        var sectionNum = document.querySelector('#sectionNum'); 

        fetch('/api/addToSchedule', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub.textContent,
                courseNumber: courseNum.textContent,
                sectionNumber: sectionNum.textContent
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            // if the server returns an error key with json it means the request failed.
            if (data.error) {
                alert(data.error);
            } else{
                console.log(data);
                setSchedule(data);
            }
        });
    }


    async function dropCourse(e){
        var sub = document.querySelector('#dropSub');
        var courseNum = document.querySelector('#dropCourseNum');
        var sectionNum = document.querySelector('#dropSection'); 

        fetch('/api/dropSection', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub.textContent,
                courseNumber: courseNum.textContent,
                sectionNumber: sectionNum.textContent
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            console.log(data);
            setRegistered(data);
        });
    }


    if(localStorage.getItem('token')) {
        return (
            <>
                <div className = {'introduction'}>
                    <h1>Registration Page</h1>
                        <p>
                        Here you can look for classes to add, update your potential schedule, or drop classes.
                        </p>
                </div>

                <div className = {'register'}>
                    <div id = {'select-register-table-div'}>
                        <h2 id={'h2-1'}> View Registered Courses or Schedules:</h2>
                        <select className= {'register-or-schedule-dropdown'} onChange={(e) => getCRDropdownValue(e)}>
                            <option >Select...</option>
                            <option value="registered-classes">Registered Courses</option>
                            <option value="schedules">Schedule</option>
                        </select>
                    </div>

                    <table className = {'registered-classes-table'}>
                        <thead>
                            <tr className = {'registered-classes-table-column-headers'}>
                                <th>Course</th>
                                <th>Subject</th>
                                <th>Course Number</th>
                                <th>Section</th>
                                <th>Days</th>     
                                <th>Capacity</th>
                                <th>Waitlist</th>
                                <th>Time</th>
                                <th>Instructor</th>
                                <th className = {'buttons-cell-header'}></th>
                            </tr>
                        </thead>
                        <tbody>
                            {registered && displayRegTable &&registered.map((regcourse, i) => (
                            <tr id = {'registered-classes-table-row'}>
                                <td>{regcourse.title}</td>
                                <td id= {'dropSub'}>{regcourse.subject}</td>
                                <td id= {'dropCourseNum'}>{regcourse.course_number}</td>
                                <td id= {'dropSection'}>{regcourse.section_number}</td>
                                <td>{regcourse.days}</td>
                                <td>{regcourse.active}/{regcourse.capacity}</td>      
                                <td>{regcourse.waitlist_active}/{regcourse.waitlist_capacity}</td>
                                <td>{regcourse.time}</td>
                                <td>{regcourse.last_name}</td>
                                <td className = {'buttons-cell'}>
                                    <input className = {'registered-courses-drop-button'} type={'button'}
                                    onClick={(e) => dropCourse(e)} value={'Drop'}/>
                                </td>   
                            </tr>
                            ))}
                            {schedule && displaySchTable && schedule.map((sch, i) => (
                            <tr id = {'scheduled-classes-table-row'}>
                                <td>{sch.title}</td>
                                <td id= {'scheduleSub'}>{sch.subject}</td>
                                <td id= {'scheduleCourseNum'}>{sch.course_number}</td>
                                <td id= {'scheduleSection'}>{sch.section_number}</td>
                                <td>{sch.days}</td>
                                <td>{sch.active}/{sch.capacity}</td>      
                                <td>{sch.waitlist_active}/{sch.waitlist_capacity}</td>
                                <td>{sch.time}</td>
                                <td>{sch.last_name}</td>
                                <td className = {'buttons-cell'}>
                                    <span className = {'schedule-table-row-buttons'}> 
                                        <input className = {'register-button-schedule'} type={'button'} value={'Register'} 
                                        onClick={(e) => registerFromScheduleTable(e)} float = "left"/>
                                        <input className = {'scheduled-courses-remove-button'} type={'button'}
                                        onClick={(e) => removeFromSchedule(e)} value={'Remove'}/>
                                    </span>
                                </td>   
                            </tr>
                            ))}
                        </tbody>
                    </table>

                    <div id = {'course-search-div'}>
                        <h2 id={'h2-2'}>Look for classes to add:</h2>
                        <div className = {'look-for-class'}>          
                            <p>Subject: </p>
                            <select className = {'subject-dropdown'} name="Subject">
                                <option value="CSC">CSC</option>
                                <option value="MAT">MAT</option>
                                <option value="PHI">PHI</option>
                                <option value="HIS">HIS</option>
                            </select>
                            <p>Course Number: </p>               
                            <select className = {'course-number-dropdown'} name="Course Number">
                                    <option value="111">111</option>
                                <option value="222">222</option>
                                <option value="333">333</option>
                                <option value="444">444</option>
                            </select>
                            <input className = {'search-button'} type={'button'} onClick={(e) => getSections(e)} value={'Search For Classes'}/>
                        </div>
                    </div>


                    <table className = {'sections-table'}>
                        <thead>
                            <tr className = {'sections-table-column-headers'}>
                                <th>Course</th>
                                <th>Subject</th>
                                <th>Course Number</th>
                                <th>Section</th>
                                <th>Days</th>      
                                <th>Capacity</th> 
                                <th>Waitlist</th>
                                <th>Time</th>
                                <th>Instructor</th>
                                <th className = {'buttons-cell-header'}></th>
                            </tr>
                        </thead>
                        <tbody> 
                            {sections && sections.map((section, i) => (
                                <tr className = {'sections-table-row'}>
                                <td>{section.title}</td>
                                <td id = {'subject'}>{section.subject}</td>
                                <td id = {'courseNum'}>{section.course_number}</td>
                                <td id = {'sectionNum'}>{section.section_number}</td>
                                <td>{section.days}</td>      
                                <td>{section.active}/{section.capacity}</td>
                                <td>{section.waitlist_active}/{section.waitlist_capacity}</td>
                                <td>{section.time}</td>
                                <td>{section.last_name}</td>
                                <td className = {'buttons-cell'}>
                                    <span className = {'sections-table-row-buttons'}> 
                                        <input className = {'register-button'} type={'button'} value={'Register'} 
                                        onClick={(e) => registerFromRegisterTable(e)} float = "left"/>
                                        <input className = {'add-to-schedule-button'} type={'button'} value={'Add to Schedule'}
                                        onClick={(e) => addToSchedule(e)} float = "left"/>
                                    </span>
                                </td>
                                </tr> 
                            ))}            
                        </tbody>           
                    </table>
                </div>    
            </>
        )
    } 
    //Display 401 error if client isn't logged in
    else  {
        return (
            401
        )
    }
}

export default Register