import React from 'react';

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.css'
import { Form, Navbar, Nav, NavDropdown, FormControl, Button } from 'react-bootstrap'

import homeList from './content.list/home/home.list'
import honorList from './content.list/honor/honor.list'
import schoolList from './content.list/school/school.list'
import loveList from './content.list/love/love.list'
import eatList from './content.list/eat/eat.list'
import freeList from './content.list/free/free.list'

function App() {
  return (
    <Router>
      <div>
        <Navbar bg="light" expand="lg">
          <Navbar.Brand href="home">가천아고라</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="honor">명예의 전당</Nav.Link>
              <NavDropdown title="찬반 게시판" id="basic-nav-dropdown">
                <NavDropdown.Item href="school">학사행정</NavDropdown.Item>
                <NavDropdown.Item href="love">연애</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="eat">오늘 뭐먹지</NavDropdown.Item>
              </NavDropdown>
              <Nav.Link href="free">자유게시판</Nav.Link>
            </Nav>
            <Form inline>
              <FormControl type="text" placeholder="Search" className="mr-sm-2" />
              <Button variant="outline-success">Search</Button>
            </Form>
          </Navbar.Collapse>
        </Navbar>
      </div>

      <div className="container mt-3">
        <Switch>
          <Route exact path={["/", "/home"]} component={homeList} />
          <Route exact path="/honor" component={honorList} />
          <Route exact path="/school" component={schoolList} />
          <Route exact path="/love" component={loveList} />
          <Route exact path="/eat" component={eatList} />
          <Route exact path="/free" component={freeList} />
        </Switch>
      </div>
    </Router >
  );
}

export default App;