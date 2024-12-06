import './Distance.css';
import ICON from '../icon';

function Distance() {
    const distance_meter = '100m';
    return (
        <div className='distance-com'>
            <div className='user-icon'>
                <ICON.userIcon />
            </div>
            <div className='meter'>{distance_meter}</div>
        </div>
    )
}

export default Distance;