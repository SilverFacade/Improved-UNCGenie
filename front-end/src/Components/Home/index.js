import "./index.scss"

const Home = () => {

    if(localStorage.getItem('token')) {
        return (
            <>
                <div className={'maindiv'}>
                   <p>have token</p>
                </div>
            </>
        )
    } else {
        return (
            <>
                <div className={'maindiv'}>
                   <p>No token</p>
                </div>
            </>
        )
    }
}

export default Home