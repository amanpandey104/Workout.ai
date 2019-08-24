import React, { Component } from 'react';
import {Switch,Route} from 'react-router-dom';
import Login from './components/Login/Login';
import SignUp from './components/SignUp/SignUp';
import Admin from './components/Admin/Admin';
import Logout from './components/Logout/Logout';
import JumpingJack from './components/jumpingJack/JumpingJack';


export default class App extends Component {
  render() {
    return (
      <div>
        <Switch>
          <Route exact path="/" component={Login}/>
          <Route path="/signup" component={SignUp}/>
          <Route path="/admin" component={Admin}/>
          <Route path="/logout" component={Logout}/>
          <Route path="/jumpingJack" component={JumpingJack}/>
        </Switch>
      </div>
    );
  }
}
