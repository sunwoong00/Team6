import './Distance.css';
import ICON from '../icon';
import { useNavigate } from "react-router-dom";
import { updateGps } from '../api/gps';

function Distance() {
    const distance_meter = '100m';

    const updateGPS = async () => {
        try {
            const response = await updateGps({ username: '', latitude: '', longitude: '' })
            console.log(response);
        } catch {
            console.log("Error login account")
        }
    };

    updateGPS();

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