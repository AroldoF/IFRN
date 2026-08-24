use std::{
    cell::RefCell,
    rc::{Rc, Weak},
};

#[derive(Debug)]
struct Node {
    value: i32,
    father: Option<Weak<RefCell<Node>>>,
    left: Option<Rc<RefCell<Node>>>,
    right: Option<Rc<RefCell<Node>>>,
}

impl Node {
    pub fn new(
        value: i32,
        father: Option<Weak<RefCell<Node>>>,
        left: Option<Rc<RefCell<Node>>>,
        right: Option<Rc<RefCell<Node>>>,
    ) -> Self {
        Self {
            value,
            father,
            left,
            right,
        }
    }

    pub fn insert(
        &mut self,
        current: &Rc<RefCell<Node>>,
        no: Node,
    ) {
        if no.value < self.value {
            match &self.left {
                Some(left) => {
                    let next = Rc::clone(left);

                    next.borrow_mut()
                        .insert(&next, no);
                }

                None => {
                    let new_node =
                        Rc::new(RefCell::new(no));

                    new_node.borrow_mut().father =
                        Some(Rc::downgrade(current));

                    self.left = Some(new_node);
                }
            }
        } else {
            match &self.right {
                Some(right) => {
                    let next = Rc::clone(right);

                    next.borrow_mut()
                        .insert(&next, no);
                }

                None => {
                    let new_node =
                        Rc::new(RefCell::new(no));

                    new_node.borrow_mut().father =
                        Some(Rc::downgrade(current));

                    self.right = Some(new_node);
                }
            }
        }
    }
}

fn main() {
    let nums = vec![
        45, 20, 60, 10,
        30, 50, 70, 25,
    ];

    let raiz = Rc::new(
        RefCell::new(
            Node::new(
                45,
                None,
                None,
                None,
            )
        )
    );

    for num in &nums[1..] {
        let current = Rc::clone(&raiz);

        raiz.borrow_mut().insert(
            &current,
            Node::new(*num, None, None, None),
        );
    }

    println!("{:#?}", raiz);
}