import React, {Component} from "react";
import data from './data';

class Form extends Component {

    constructor() {
        super();
        this.state = {
            data: data,
        };
    };

    render() {
        return (
            <div className="container">
                <div className="row justify-content-center">
                    <div className="col-md-10">
                        <div className="card text-muted font-weight-bold">
                            <div className="card-header">
                                {this.state.data.name}
                            </div>
                            <div className="card-body">
                                <form encType="multipart/form-data" method="post"
                                      className="form-horizontal">
                                    <p><label htmlFor="id_date">Дата:</label> <input type="text" name="date" required
                                                                                     id="id_date"/></p>
                                    <p><label htmlFor="id_number">Нумар:</label> <input type="number" name="number"
                                                                                        required id="id_number"/></p>
                                    <p><label htmlFor="id_priest">Святар:</label> <select name="priest" required
                                                                                          id="id_priest">
                                        <option value="" selected>---------</option>

                                        <option value="3">іярэй Ігар Данільчык</option>

                                        <option value="4">протаярэй Аляксандр Балоннікаў</option>

                                    </select></p>
                                    <p><label htmlFor="id_certificate">Файл пасведчання:</label> <input type="file"
                                                                                                        name="certificate"
                                                                                                        id="id_certificate"/>
                                    </p>
                                    <p><label htmlFor="id_baptized_name">Імя ахрышчанага:</label> <input type="text"
                                                                                                         name="baptized_name"
                                                                                                         maxLength="30"
                                                                                                         required
                                                                                                         id="id_baptized_name"/>
                                    </p>
                                    <p><label htmlFor="id_baptized_middle_name">Імя па бацьку ахрышчанага:</label>
                                        <input type="text" name="baptized_middle_name" maxLength="30"
                                               id="id_baptized_middle_name"/></p>
                                    <p><label htmlFor="id_baptized_surname">Прозвішча ахрышчанага:</label> <input
                                        type="text" name="baptized_surname" maxLength="30" required
                                        id="id_baptized_surname"/></p>
                                    <p><label htmlFor="id_godfather">Хросны бацька:</label> <input type="text"
                                                                                                   name="godfather"
                                                                                                   maxLength="100"
                                                                                                   id="id_godfather"/>
                                    </p>
                                    <p><label htmlFor="id_godmother">Хросная маці:</label> <input type="text"
                                                                                                  name="godmother"
                                                                                                  maxLength="100"
                                                                                                  id="id_godmother"/>
                                    </p>
                                    <p><label htmlFor="id_saint_name">Імя святога:</label> <input type="text"
                                                                                                  name="saint_name"
                                                                                                  maxLength="300"
                                                                                                  id="id_saint_name"/>
                                    </p>
                                    <p><label htmlFor="id_saint_date">Дзень Анёла:</label> <input type="text"
                                                                                                  name="saint_date"
                                                                                                  id="id_saint_date"/>
                                    </p>
                                    <input className="btn btn-primary" type="submit" value="Submit"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );

    }

}

export default Form