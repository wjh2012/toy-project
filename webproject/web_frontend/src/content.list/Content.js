import React from 'react'

function Content({ title, contents, createdAt, updatedAt }) {
    return (
        <tr>
            <td><a href='#'>{title}</a></td>
            <td>{contents}</td>
            <td>{createdAt}</td>
            <td>{updatedAt}</td>
        </tr>
    )
}

export default Content