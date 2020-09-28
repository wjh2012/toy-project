import React from 'react'
import { Form, Button } from 'react-bootstrap'

class ContentForm extends React.Component {
  state = {

  }

  render() {
    return (
      <div>
        <div>
          <Form>
            <Form.Group controlId="exampleForm.ControlInput1">
              <Form.Label>Title</Form.Label>
              <Form.Control as="textarea" rows="1" />
            </Form.Group>

            <Form.Group controlId="exampleForm.ControlTextarea1">
              <Form.Label>Contents</Form.Label>
              <Form.Control as="textarea" rows="10" />
            </Form.Group>
          </Form>
        </div>
        <div>
          <Button variant="outline-primary">완료</Button>{' '}
        </div>
      </div>

    )
  }
}

export default ContentForm