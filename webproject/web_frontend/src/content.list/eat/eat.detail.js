import React from "react";
import axios from "axios";


class eatDetail extends React.Component {
    state = {
        id : null
    }

    getContents = async () => {
        
        const url = 'api/db/board/eat'+this.props.id
        const contents = await axios.get(url);
        this.setState({ contents: contents.data });
        console.log(contents);
    };

    componentDidMount() {
        this.getContents();
    }

    render(){
        return(
            <div>
                
            </div>
        )
    }
}

export default eatDetail;