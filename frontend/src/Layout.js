import React, {Component} from 'react';
import data from './data';
import FullName from './FulName';
import './App.css';


class Layout extends Component {

    constructor(){
        super();
        this.state = {
            data: data,
        };
    };

    componentWillMount() {
        this.setState({
            fullname: data,
        })
    };

    addFullName = (e) => {
        e.preventDefault();
        const fullname = this.state.fullname
        this.setState({
            fullname: fullname.concat({ name:'', surname: ''})
        });

        console.log('Clicked!');
    };

    render() {
        return (
            <div className="App">
                <a href='#' className="btn btn-primary" onClick={this.addFullName}>Add full name</a>
                    {this.state.fullname.map(info =>
                        <FullName key={info.id} {...info}/>
                    )}
            </div>

        );
    }
}

export default Layout;
