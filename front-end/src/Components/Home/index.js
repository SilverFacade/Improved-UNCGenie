import "./index.scss"
import {useState, useEffect} from "react";

const Home = () => {
    async function home(e) {
        e.preventDefault();
        const user = document.querySelector('form [name="username"]');
        const pass = document.querySelector('form [name="password"]');
    const request = await fetch('/api/home', {
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
        window.location.href = '/home';
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

    return (
        <>
            <form className={'todo'} onSubmit={(e) => AddToList(e)} id={'todo'}>
                <span>
                    {
                        initState.map((task) => (<div onClick={(e)=>e.target.remove()}> {task}</div>))
                    }
                </span>
                <input type={'text'} placeholder={'Enter Task Here'} id={'taskinput'} required/>
                <input type={'submit'} value={'Add To List'}/>
            </form>

            <form className={'registerhere'} id={'registerhere'}>
            <a href={'/register'}>
                Register!
            </a>
            </form>

            <form className={'currentschedule'} onSubmit={(e) => home(e)} id={'currentschedule'}>
                <input type={'text'} placeholder={'Current Schedule Display'} name={'username'} required/>
            </form>

            <form className={'degreeprogress'} onSubmit={(e) => home(e)} id={'degreeprogress'}>
                <input type={'submit'} value={'View Progress'}/>
            </form>
        </>
    )
}

export default Home