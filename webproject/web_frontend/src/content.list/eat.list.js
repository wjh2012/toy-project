import React from "react";
import axios from "axios";

import 'bootstrap/dist/css/bootstrap.css'
import Content from "./Content";

class eatList extends React.Component {
  state = {
    contents: [],
  };

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
              <Content
                key={item._id}
                title={item.title}
                contents={item.contents}
                createdAt={item.createdAt}
                updatedAt={item.updatedAt}
              />)
            )}
          </tbody>
        </table>       
      </div>
    )
  }
}
export default eatList;
