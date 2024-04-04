import { useState } from "react";
import "./index.scss"
import Nav from '../Nav';

let displayRegTable = false;
let displaySchTable = false;

const Register = () => {
    const [sections, setSections] = useState(null);
    const [schedule, setSchedule] = useState(null);
    const [registered, setRegistered] = useState(null);
    
    
    async function getSections(e){
        let sub = document.querySelector('.subject-dropdown');
        let courseNum = document.querySelector('.course-number-dropdown');

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
        let dropDownValue = document.querySelector('.register-or-schedule-dropdown');

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


    async function registerFromScheduleTable(e, sub, courseNum, sectionNum){
        fetch('/api/register', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub,
                courseNumber: courseNum,
                sectionNumber: sectionNum
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            if (data.error) {
                alert(data.error);
            } else{
                console.log(data);
                setRegistered(data);
            }
        });
    }


    async function removeFromSchedule(e, sub, courseNum, sectionNum){
        fetch('/api/removeFromSchedule', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub,
                courseNumber: courseNum,
                sectionNumber: sectionNum
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            console.log(data);
            setSchedule(data);
        });
    }

    
    async function registerFromRegisterTable(e, sub, courseNum, sectionNum){
        fetch('/api/register', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub,
                courseNumber: courseNum,
                sectionNumber: sectionNum
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

    
    async function addToSchedule(e, sub, courseNum, sectionNum){
        fetch('/api/addToSchedule', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub,
                courseNumber: courseNum,
                sectionNumber: sectionNum
            })
        }).then(res=> {
            return res.json()
        }).then(data => {
            if (data.error) {
                alert(data.error);
            } else{
                console.log(data);
                setSchedule(data);
            }
        });
    }

    
    async function dropCourse(e, sub, courseNum, sectionNum){
        fetch('/api/dropSection', 
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "token": localStorage.getItem('token')
            }, 
            body: JSON.stringify({
                subject: sub,
                courseNumber: courseNum,
                sectionNumber: sectionNum
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
                <Nav/>
                <div className = {'introduction'}>
                    <h1>Registration Page</h1>
                        <p>
                        Here you can look for classes to add, add sections to a list of potential classes to register for, or drop classes.
                        </p>
                </div>

                <div className = {'register'}>
                    <div id = {'select-register-table-div'}>
                        <h2 id={'h2-1'}> View Registered Courses or Schedules:</h2>
                        <select className= {'register-or-schedule-dropdown'} onChange={(e) => getCRDropdownValue(e)}>
                            <option >Select...</option>
                            <option value="registered-classes">Registered Courses</option>
                            <option value="schedules">Watched Classes</option>
                        </select>
                    </div>

                    <table className = {'registered-classes-table'}>
                        <thead>
                            <tr className = {'registered-classes-table-column-headers'}>
                                <th className = {'data-cell-header'}>CRN</th>
                                <th className = {'data-cell-header'}>Course</th>
                                <th className = {'data-cell-header'}>Subject</th>
                                <th className = {'data-cell-header'}>Course Number</th>
                                <th className = {'data-cell-header'}>Section</th>
                                <th className = {'data-cell-header'}>Days</th>     
                                <th className = {'data-cell-header'}>Capacity</th>
                                <th className = {'data-cell-header'}>Waitlist</th>
                                <th className = {'data-cell-header'}>Time</th>
                                <th className = {'data-cell-header'}>Instructor</th>
                                <th className = {'buttons-cell-header'}></th>
                            </tr>
                        </thead>
                        <tbody>
                            {registered && displayRegTable && registered.map((regcourse, i) => (
                            <tr id = 'registered-classes-table-row' key={i}>
                                <td className = {'data-cell'}>{regcourse.crn}</td>
                                <td className = {'data-cell'} style={{fontSize: "12px"}}>{regcourse.title}</td>
                                <td className = {'data-cell'}>{regcourse.subject}</td>
                                <td className = {'data-cell'}>{regcourse.course_number}</td>
                                <td className = {'data-cell'}>{regcourse.section_number}</td>
                                <td className = {'data-cell'}>{regcourse.days}</td>
                                <td className = {'data-cell'}>{regcourse.active}/{regcourse.capacity}</td>      
                                <td className = {'data-cell'}>{regcourse.waitlist_active}/{regcourse.waitlist_capacity}</td>
                                <td className = {'data-cell'} style={{fontSize: "14px"}}>{regcourse.start_time}-{regcourse.end_time}</td>
                                <td className = {'data-cell'}>{regcourse.last_name}</td>
                                <td className = {'buttons-cell'}>
                                    <input className = {'registered-courses-drop-button'} type={'button'}
                                    onClick={(e) => dropCourse(e, regcourse.subject, regcourse.course_number, regcourse.section_number)} value={'Drop'}/>
                                </td>   
                            </tr>
                            ))}
                            {schedule && displaySchTable && schedule.map((sch, i) => (
                            <tr id = {'scheduled-classes-table-row'} key={i}>
                                <td className = {'data-cell'}>{sch.crn}</td>
                                <td className = {'data-cell'} style={{fontSize: "12px"}}>{sch.title}</td>
                                <td className = {'data-cell'}>{sch.subject}</td>
                                <td className = {'data-cell'}>{sch.course_number}</td>
                                <td className = {'data-cell'}>{sch.section_number}</td>
                                <td className = {'data-cell'}>{sch.days}</td>
                                <td className = {'data-cell'}>{sch.active}/{sch.capacity}</td>      
                                <td className = {'data-cell'}>{sch.waitlist_active}/{sch.waitlist_capacity}</td>
                                <td className = {'data-cell'} style={{fontSize: "14px"}}>{sch.start_time}-{sch.end_time}</td>
                                <td className = {'data-cell'}>{sch.last_name}</td>
                                <td className = {'buttons-cell'}>
                                        <input className = {'register-button-schedule'} type={'button'}  
                                        onClick={(e) => registerFromScheduleTable(e, sch.subject, sch.course_number, sch.section_number)} value={'Register'} float = "left"/>
                                        <input className = {'scheduled-courses-remove-button'} type={'button'}
                                        onClick={(e) => removeFromSchedule(e, sch.subject, sch.course_number, sch.section_number)}  value={'Remove'}/>
                                 
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
                                <option value="BIO">BIO</option>
                                <option value="PHY">PHY</option>
                                <option value="FRE">FRE</option>
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
                                <th className = {'data-cell-header'}>CRN</th>
                                <th className = {'data-cell-header'}>Course</th>
                                <th className = {'data-cell-header'}>Subject</th>
                                <th className = {'data-cell-header'}>Course Number</th>
                                <th className = {'data-cell-header'}>Section</th>
                                <th className = {'data-cell-header'}>Days</th>      
                                <th className = {'data-cell-header'}>Capacity</th> 
                                <th className = {'data-cell-header'}>Waitlist</th>
                                <th className = {'data-cell-header'}>Time</th>
                                <th className = {'data-cell-header'}>Instructor</th>
                                <th className = {'buttons-cell-header'}></th>
                            </tr>
                        </thead>
                        <tbody> 
                            {sections && sections.map((section, i) => (
                            <tr className = {'sections-table-row'} key={i}>
                                <td className = {'data-cell'}>{section.crn}</td>
                                <td className = {'data-cell'} style={{fontSize: "12px"}}>{section.title}</td>
                                <td className = {'data-cell'}>{section.subject}</td>
                                <td className = {'data-cell'}>{section.course_number}</td>
                                <td className = {'data-cell'}>{section.section_number}</td>
                                <td className = {'data-cell'}>{section.days}</td>      
                                <td className = {'data-cell'}>{section.active}/{section.capacity}</td>
                                <td className = {'data-cell'}>{section.waitlist_active}/{section.waitlist_capacity}</td>
                                <td className = {'data-cell'} style={{fontSize: "14px"}}>{section.start_time}-{section.end_time}</td>
                                <td className = {'data-cell'}>{section.last_name}</td>
                                <td className = {'buttons-cell'}>
                                    <span className = {'sections-table-row-buttons'}> 
                                        <input className = {'register-button'} type={'button'} value={'Register'} 
                                        onClick={(e) => registerFromRegisterTable(e, section.subject, section.course_number, section.section_number)} float = "left"/>
                                        <input className = {'add-to-schedule-button'} type={'button'} value={'Add to Watched'}
                                        onClick={(e) => addToSchedule(e, section.subject, section.course_number, section.section_number)} float = "left"/>
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
    // Display 401 error if client isn't logged in
    else  {
        return (
            <div className={'loginRequired'}>
                <p>You must Login</p>
            </div>
        )
    }
}

export default Register