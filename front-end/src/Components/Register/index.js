import { useState } from "react";
import "./index.scss"

const Register = () => {
    const [sections, setSections] = useState(null);
    var sub = document.querySelector('.subject-dropdown');
    var courseNum = document.querySelector('.course-number-dropdown');

    async function generateSections(e){
        e.preventDefault();

        fetch('/api/sections', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                subject: sub.value,
                courseNumber: courseNum.value
            })
        }).then(res=> {
            return res.json();
        }).then(data => {
            console.log(data);
            setSections(data);
        });
    }
    

    return (
        <>
            <div className = {'introduction'}>
                <h1>Registration Page</h1>
                <p>
                    Here you can look for classes to add, update your schedules, or drop classes.
                </p>
            </div>

            <div className = {'register'}>
                <h2 align="center"> Registered Courses/Schedules:</h2>
                <select className= {'register-or-schedule-button'}>
                    <option value="registered-classNamees">Registered Courses</option>
                    <option value="schedules">Schedules</option>
                </select>

                <table className = {'registered-classes-table'}>
                    <thead>
                        <tr className = {'registered-classes-table-column-headers'}>
                            <th>className</th>
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
                        <tr className = {'registered-classes-table-row'}>
                            <td>className</td>
                            <td>CSC</td>
                            <td>490</td>
                            <td>01</td>
                            <td>TTH</td>
                            <td>12 / 15</td>      
                            <td>0/5</td>
                            <td>8:00-9:15am</td>
                            <td>Mr. Smith</td>
                            <td className = {'buttons-cell'}>
                                <input className = {'registered-courses-drop-button'} type={'button'} value={'Drop'}/>
                            </td>   
                        </tr>
                    </tbody>
                </table>

                <h2 align = "center">Look for classes to add:</h2>
                <div className = {'look-for-class'}>          
                    <p>Subject: </p>
                    <select className = {'subject-dropdown'} name="Subject" id="subject">
                        <option value="CSC">CSC</option>
                        <option value="MAT">MAT</option>
                        <option value="PHI">PHI</option>
                        <option value="HIS">HIS</option>
                    </select>
                    <p>Course Number: </p>               
                    <select className = {'course-number-dropdown'} name="Course Number" id="course_number">
                        <option value="111">111</option>
                        <option value="222">222</option>
                        <option value="333">333</option>
                        <option value="444">444</option>
                    </select>
                    <input className = {'search-button'} type={'button'} onClick={(e) => generateSections(e)} value={'Search For Classes'}/>
                </div>

                <table className = {'sections-table'}>
                    <thead>
                        <tr className = {'sections-table-column-headers'}>
                            <th>className</th>
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
                            <td>ClassName</td>
                            <td>{section.subject}</td>
                            <td>{section.course_number}</td>
                            <td>{section.section_number}</td>
                            <td>{section.days}</td>      
                            <td>{section.active}/{section.capacity}</td>
                            <td>{section.waitlist_active}/{section.waitlist_capacity}</td>
                            <td>{section.time}</td>
                            <td>Instructor</td>
                            <td className = {'buttons-cell'}>
                                <span className = {'sections-table-row-buttons'}> 
                                    <input className = {'register-button'} type={'button'} value={'Register'} float = "left"/>
                                <input className = {'add-to-schedule-button'} type={'button'} value={'Add to Schedule'} float = "left"/>
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

export default Register