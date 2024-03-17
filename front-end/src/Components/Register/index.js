import "./index.scss"

const Register = () => {
    // TODO: Add API requests


    return (
        <>
            <div class = {'register'}>
                <h1 align="center">Registration Page</h1>
                <p align="center">
                    Here you can look for classes to add, update your schedules, or drop classes.
                </p>
                <h2 align="center"> Registered Classes/Schedules:</h2>
                <select class= {'register-or-schedule-button'}>
                    <option value="registered-classes">Registered Classes</option>
                    <option value="schedules">Schedules</option>
                </select>

                <table class = {'registered-classes-table'}>
                    <tr class = {'registered-classes-table-column-headers'}>
                        <th>ClassName</th>
                        <th>Subject</th>
                        <th>Course Number</th>
                        <th>Section</th>
                        <th>Days</th>     
                        <th>Capacity</th>
                        <th>Waitlist</th>
                        <th>Time</th>
                        <th>Instructor</th>
                    </tr>
                    <tr class = {'registered-classes-table-row'}>
                        <td>ClassName</td>
                        <td>CSC</td>
                        <td>490</td>
                        <td>01</td>
                        <td>TTH</td>
                        <td>12 / 15</td>      
                        <td>0/5</td>
                        <td>8:00-9:15am</td>
                        <td>Mr. Smith</td>
                        <input class = {'drop-button'} type={'button'} value={'Drop'}/>
                    </tr>
                    <tr class = {'registered-classes-table-row'}>
                        <td>ClassName</td>
                        <td>CSC</td>
                        <td>490</td>
                        <td>01</td>
                        <td>TTH</td>
                        <td>12 / 15</td>
                        <td>0/5</td>
                        <td>8:00-9:15am</td>
                        <td>Mr. Smith</td>
                        <input class = {'drop-button'} type={'button'} value={'Drop'}/>
                    </tr>
                </table>

                <h2 align = "center">Look for classes to add:</h2>
                <div class = {'look-for-class'}>          
                    <p>Subject: </p>
                    <select class = {'subject-dropdown'} name="Subject" id="subject">
                        <option value="CSC">CSC</option>
                        <option value="MAT">MAT</option>
                        <option value="PHI">PHI</option>
                        <option value="HIS">HIS</option>
                    </select>
                    <p>Course Number: </p>               
                    <select class = {'course-number-dropdown'} name="Course Number" id="course_number">
                        <option value="111">111</option>
                        <option value="222">222</option>
                        <option value="333">333</option>
                        <option value="444">444</option>
                    </select>
                    <input class = {'search-button'} type={'submit'} value={'Search For Classes'}/>
                </div>


                <table class = {'sections-table'}>
                    <tr class = {'sections-table-column-headers'}>
                        <th>ClassName</th>
                        <th>Subject</th>
                        <th>Course Number</th>
                        <th>Section</th>
                        <th>Days</th>      
                        <th>Capacity</th> 
                        <th>Waitlist</th>
                        <th>Time</th>
                        <th>Instructor</th>
                    </tr>
                    <tr class = {'sections-table-row'}>
                        <td>ClassName</td>
                        <td>CSC</td>
                        <td>490</td>
                        <td>01</td>
                        <td>TTH</td>      
                        <td>12 / 15</td>
                        <td>0/5</td>
                        <td>8:00-9:15am</td>
                        <td>Mr. Smith</td>
                        <div class = {'sections-table-row-buttons'}> 
                            <input class = {'register-button'} type={'button'} value={'Register'} float = "left"/>
                            <input class = {'add-to-schedule-button'} type={'button'} value={'Add to Schedule'} float = "left"/>  
                        </div>
                    </tr> 
                    <tr class = {'sections-table-row'}>
                        <td>ClassName</td>
                        <td>CSC</td>
                        <td>490</td>
                        <td>01</td>
                        <td>TTH</td>
                        <td>12 / 15</td>
                        <td>0/5</td>
                        <td>8:00-9:15am</td>
                        <td>Mr. Smith</td>
                        <div class = {'sections-table-row-buttons'}> 
                            <input class = {'register-button'} type={'button'} value={'Register'} float = "left"/>
                            <input class = {'add-to-schedule-button'} type={'button'} value={'Add to Schedule'} float = "left"/>
                        </div>
                    </tr>           
                </table>
            </div>
        </>
    )
}

export default Register