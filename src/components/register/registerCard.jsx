import React, { Fragment } from 'react';
import styles from './css/register.module.css';
import clsx from 'clsx';
import './css/style.css';

function RegisterCard() {
    return (
        <div>
            <div className={clsx(styles.margTop)}>
                <div className={clsx("card", styles.reg_card)}>
                    <div className={clsx(styles.loginCardPadding)}>
                        <div className={clsx("card", styles.logincard)}>
                            Login Here
                        </div>
                    </div>
                    <div className='form-group m-2'>
                        <input className='form-control' type="text" placeholder="Email or Phone number" />
                    </div>
                    <div className='form-group m-2'>
                        <input className='form-control' type="password" placeholder="Password" />
                    </div>
                    <div className='form-group m-2'>
                        <button className='btn btn-dark'>Sign in</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default RegisterCard;