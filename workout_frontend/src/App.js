import React, { Component } from 'react';
import {Switch,Route} from 'react-router-dom';
import Login from './components/Login/Login';
import Admin from './components/Admin/Admin';
import Logout from './components/Logout/Logout';

export default class App extends Component {
  render() {
    return (
      <div>
        <Switch>
          <Route exact path="/" component={Login}/>
          <Route path="/admin" component={Admin}/>
          <Route path="/logout" component={Logout}/>
        </Switch>
      </div>
    );
  }
}
