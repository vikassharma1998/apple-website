import React, { Component } from 'react';
import { render } from 'react-dom';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        };
    }

    componentDidMount() {
        fetch('apple_iphone/api')
        .then(response => {
            if (response.status >400){
                return this.setState(() => {
                    return {placeholder : "Something went wrong!"}
                });
            }
            return response.json();
        })
        .then (data => {
            this.setState(()=> {
                return {
                    data,
                    loaded : true
                };
            });
        });
    }

    render() {
        return (
            <ul>
                {this.state.data.map(apple_iphone=>{
                    return (
                        <li key = {apple_iphone.id}>
                            {apple_iphone.name} - {apple_iphone.description}
                        </li>
                    );
                })}
            </ul>
        );
    }
}