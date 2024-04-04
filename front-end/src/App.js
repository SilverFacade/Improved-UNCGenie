import logo from './logo.svg';
import './App.css';
import {useEffect} from 'react';
import {Routes, Route} from "react-router-dom";
import Home from './Components/Home';
import Login from './Components/Login';
import Register from './Components/Register';
import ClassInfo from './Components/ClassInfo';
import Personal from './Components/PersonalInfo';
import Progress from './Components/Progress';
import NotFound from './Components/NotFound';

function App() {
    /* figure out how to clear local storage on tab close
    useEffect(() => {
        return () => {
          window.addEventListener("unload", function(e) {
    
          let confirmationMessage = "o/";

          localStorage.clear();
    
          (e || window.event).returnValue = confirmationMessage; //Gecko + IE
    
          console.log("logout !");
          return confirmationMessage; //Webkit, Safari, Chrome
        
        });
       } 
    });
    */

  return (
      <>
          <div className={'wrapper'}>
              <Routes>
                  <Route path = {'/'} element = {<Home />} />
                  <Route path = {'/login'} element = {<Login />} />
                  <Route path = {'/register'} element = {<Register />} />
                  <Route path = {'/classInfo'} element = {<ClassInfo />} />
                  <Route path = {'/progress'} element = {<Progress />} />
                  <Route path = {'/personal'} element = {<Personal />} />
                  <Route path = {'*'} element = {<NotFound />} />
              </Routes>
          </div>
      </>
  );
}

export default App;
