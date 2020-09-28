import React from "react";
import axios from "axios";
import {Link, Route} from 'react-router-dom'
import eatDetail from './eat.detail'

class eatList extends React.Component {
  state = {
    contents: [],
  };

  showsummary = ({ key, title, contents, createdAt, updatedAt }) => {
    return (
      <tr>
        <td>{title}</td>
        <td>{contents}</td>
        <td>{createdAt}</td>
        <td>{updatedAt}</td>
      </tr>
    )
  }

  getContents = async () => {
    const contents = await axios.get("api/db/board/eat");
    this.setState({ contents: contents.data });
    console.log(contents);
  };

  componentDidMount() {
    this.getContents();
  }

  render() {
    const { contents } = this.state
    return (
      <div className='container'>
        <table className='table table-striped'>
          <thead>
            <tr>
              <th>제목</th>
              <th>내용</th>
              <th>작성일</th>
              <th>수정일</th>
            </tr>
          </thead>
          <tbody>
            {contents.map(item => (
              <this.showsummary
                key={item._id}
                title={item.title}
                contents={item.contents}
                createdAt={item.createdAt}
                updatedAt={item.updatedAt}
              />
            )
            )}
          </tbody>
        </table>
      </div>
    )
  }
}
export default eatList;
