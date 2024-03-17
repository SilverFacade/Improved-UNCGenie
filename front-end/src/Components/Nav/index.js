import "./index.scss"
import {Link} from "react-router-dom";
//import LogoS from '../../assets/images/logo-s.png'
//import LogoSubtitle from '../../assets/images/logo_sub.png'

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faHome, faEnvelope, faUser, faArrowRightToBracket, faDoorOpen} from '@fortawesome/free-solid-svg-icons'
import { faSkype, faYoutube, faGithub, faLinkedin } from '@fortawesome/free-brands-svg-icons'
import {NavLink} from "react-router-dom";

let ex = "Jello :) :) Yippee"
//faDoorOpen
const Nav = () => {
    function logout() {
        localStorage.clear();
        window.location.href=window.location.path;
    }

    const element = localStorage.getItem('token') ?
        (
            <a onClick={()=>logout()}>
                <FontAwesomeIcon icon={faDoorOpen}/>
            </a>
        )
        :
        (
            <a href='/login'>
                <FontAwesomeIcon icon={faArrowRightToBracket}/>
            </a>
        );

    
    return (
        <>
            <nav className={'nav-bar'}>
                <span className={'logos'}>
                    <Link className='logo' to='/'>
                         <img src={''} alt="logo"/>
                         {/* <img className="sub-logo" src={''} alt="logo"/> */}
                    </Link>
                </span>
                <span className={'first-three'}>
                    <NavLink exact="true" activeclassname="active" to="/home">
                        <FontAwesomeIcon icon={faHome} />
                    </NavLink>
                    <NavLink exact="true" activeclassname="active" className="about-link" to="/about">
                        <FontAwesomeIcon icon={faUser} />
                    </NavLink>
                    <NavLink exact="true" activeclassname="active" className="contact-link" to="/contact">
                        <FontAwesomeIcon icon={faEnvelope} />
                    </NavLink>
                </span>
                <span className={'span-end'}>
                    { element }
                    <a
                        href=''
                    >
                        <FontAwesomeIcon icon={faGithub} />
                    </a>
                    <a
                        href=''
                    >
                        <FontAwesomeIcon icon={faYoutube} />
                    </a>
                    <a
                        href=''
                    >
                        <FontAwesomeIcon icon={faSkype} />
                    </a>
                </span>
            </nav>
        </>
    );
}

export default Nav;