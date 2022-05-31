import React from 'react';
import styles from './css/register.module.css';
import clsx from 'clsx';
import './css/style.css';
import padlock from './icons/padlock.png';
import { Link } from 'react-router-dom';

function RegisterCard() {
    return (
        <div>
            <div className={clsx(styles.margTop)}>
                <div className={clsx("card", styles.reg_card)}>
                    <div className={clsx(styles.loginCardPadding)}>
                        <div className={clsx("card container text-center", styles.logincard)}>
                            <div className={clsx(styles.icondiv)}>
                            <img className={clsx(styles.icon, )} src={padlock} alt="" srcset="" />
                            </div>
                            Login Here
                        </div>
                    </div>
                    <div className='form-group m-2'>
                        <input className='form-control text-center' type="text" placeholder="Email*" />
                    </div>
                    <div className='form-group m-2'>
                        <input className='form-control text-center' type="password" placeholder="Password*" />
                    </div>
                    <div className='form-group m-2'>
                        <button className='btn btn-dark'>Sign in</button>
                    </div>
                    <div>
                        <h6><Link to ='/forgotpassword' >Forgot Password</Link></h6>
                    </div>
                </div>
            </div>
        </div >
    );
}

export default RegisterCard;