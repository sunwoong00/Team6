import './CallingOption.css';
import ICON from '../icon';

function CallingOption() {

    return (
        <div className='icon-grid'>
            {/* 블루투스 아이콘 */}
            <div className='icon-item'>
                <ICON.bluetoothIcon />
            </div>
            {/* 비디오 아이콘 */}
            <div className='icon-item'>
                <ICON.videoIcon />
            </div>
            {/* 볼륨 아이콘 */}
            <div className='icon-item'>
                <ICON.volumeIcon />
            </div>
            {/* callover 아이콘 */}
            <div className='icon-item'>
                <ICON.calloverIcon />
            </div>
        </div>
    )
}

export default CallingOption;