import React from 'react';

const FullName = props =>
    <div class="card">
        <div class="card-header">Full name</div>
        <div class="card-body">
            <p>{props.name} {props.surname}</p>
        </div>
    </div>;

export default FullName;