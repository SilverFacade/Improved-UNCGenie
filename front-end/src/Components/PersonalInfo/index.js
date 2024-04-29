import "./index.scss"
import Nav from '../Nav';
import {useState, useEffect} from "react";

const PersonalInfo = () => {
    const [student, setStudent] = useState(null);

    useEffect(() => {
        fetch('http://54.242.126.185:8080/api/student', {
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
      
    return (
        <>
            <Nav/>
            <div id={'infoDiv'}>
                {student && <h1>{student[0].first_name} {student[0].last_name} Personal Information</h1>}
                {student && <p> Major: {student[0].major_name}</p>}
                {student && <p> Minor: {student[0].minor_name}</p>}   
                {student && <p> Year: {student[0].year}</p>}   
                {student && <p> PIN: {student[0].pin}</p>} 
                {student && <p> Address: {student[0].address}</p>}
                {student && <p> Email: {student[0].email}</p>}        
                {student && <p> Phone: {student[0].phone_number}</p>}
                {student && <p> Emergency Contact: {student[0].emergency_contact}</p>}
                <a href="/">
                    <button type = "button" id={'homeButton'}>Ok</button>
                </a>
            </div>      
        </>
    )
}

export default PersonalInfo
