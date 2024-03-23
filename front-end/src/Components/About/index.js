import "./index.scss"
import Nav from '../Nav';

const About = () => {

    async function about(e){
        e.preventDefault();
        const user = document.querySelector('form [name="username"]');
        const pass = document.querySelector('form [name="password"]');
        //baby's first API request :) :)
        // backend needs user, pass (strings),
        // backend returns message, redirect, status
        // Backend endpoint/route: /api/login
        // Backend request method: Post

        // JS func that makes api call
        // Api calls are get and post requests
        // Get request is default
        // Get asks from server
        // Post changes something from server
        // Api call relies on server to send information
        // So gotta wait on server :( so sad

        const request = await fetch('/api/about', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: user.value,
                password: pass.value
            }) // curls for defining json objects & params when talking about data types
        }).then((res)=>res.json()); //it needs a json object as second variable
        if(request.status===200){
            localStorage.setItem('token', request.token); // Holds onto the data locally
            window.location.href='/home';
        }
        else alert(request.message); //later replace with modal (mode el)

        //console.log(request.token);
        //window.location.href='/home';
    }

    

    
    return (
        <>
            <Nav/>
            <form className={'login'} onSubmit={(e) => about(e)} id={'login'}>
                <input type={'text'} placeholder={'Username'} name={'username'} required/>
                <input type={'password'} placeholder={'Password'} name={'password'} required/>
                <input type={'submit'} value={'Login'}/>
            </form>
            <form className={'signup'} onSubmit={(e) => about(e)} id={'signup'}>
                <input type={'text'} placeholder={'Username'} name={'username'} required/>
                <input type={'password'} placeholder={'Password'} name={'password'} required/>
                <input type={'submit'} value={'Sign Up'}/>
            </form>
        </>
    )
}

export default About