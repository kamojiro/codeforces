#![allow(non_snake_case)]
fn main() {
    let s = std::io::stdin();
    let mut sc = Scanner { stdin: s.lock() };
    let n:usize = sc.read();
    let S:Vec<char> = sc.chars();
    let mut b:usize = 0;
    let mut w:usize = 0;
    let mut T:Vec<usize> = vec![];

    for i in 0..n{
        if S[i] == 'B'{
            b += 1;
            T.push(0);
        }else{
            w += 1;
            T.push(1);
        }
    }
    if (b%2 == 1) && (w%2 == 1){
        println!("-1");
        return
    }
    let mut count:usize = 0;
    let mut ans:Vec<usize> = vec![];

    if b%2 == 1{
        for i in 0..(n-1){
            if T[i] == 0{
                continue
            }
            T[i] = 0;
            T[i+1] = 1-T[i+1];
            count += 1;
            ans.push(i+1);
        }
    }else{
        for i in 0..(n-1){
            if T[i] == 1{
                continue
            }
            T[i] = 1;
            T[i+1] = 1-T[i+1];
            count += 1;
            ans.push(i+1);
        }
    }

    println!("{}", count);
    if count == 0{
        return
    }
    for i in 0..(ans.len()){
        print!("{} ", ans[i]);
    }
    println!("");
}

pub struct Scanner<R> {
    stdin: R,
}

impl<R: std::io::Read> Scanner<R> {
    pub fn read<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        let buf = self
            .stdin
            .by_ref()
            .bytes()
            .map(|b| b.unwrap())
            .skip_while(|&b| b == b' ' || b == b'\n')
            .take_while(|&b| b != b' ' && b != b'\n')
            .collect::<Vec<_>>();
        unsafe { std::str::from_utf8_unchecked(&buf) }
        .parse()
            .ok()
            .expect("Parse error.")
    }
    pub fn vec<T: std::str::FromStr>(&mut self, n: usize) -> Vec<T> {
        (0..n).map(|_| self.read()).collect()
    }
    pub fn chars(&mut self) -> Vec<char> {
        self.read::<String>().chars().collect()
    }
}


