import java.awt.event.*;
import javax.swing.*;

class Registeraion extends JFrame implements ActionListener {

  private static final long serialVersionUID = 1L;
  JFrame f = new JFrame("Registeration Form");
  JRadioButton rb1, rb2, rb3, rb4;
  JButton b;
  JLabel l1, l2, l3, l4;
  JCheckBox chb1;
  JTextField t1, t2, t3, t4;

  Registeraion() {
    l1 = new JLabel("Name");
    l1.setBounds(30, 25, 100, 30);
    t1 = new JTextField();
    t1.setBounds(90, 30, 100, 20);

    l2 = new JLabel("Roll no");
    l2.setBounds(30, 50, 100, 30);
    t2 = new JTextField();
    t2.setBounds(90, 55, 100, 20);
    l3 = new JLabel("Batch");
    l3.setBounds(30, 75, 100, 30);
    t3 = new JTextField();
    t3.setBounds(90, 80, 100, 20);
    l4 = new JLabel("Branch");
    l4.setBounds(30, 100, 100, 30);
    t4 = new JTextField();
    t4.setBounds(90, 105, 100, 20);
    rb1 = new JRadioButton("CSE");
    rb1.setBounds(30, 130, 100, 30);
    rb2 = new JRadioButton("ECE");
    rb2.setBounds(80, 130, 100, 30);
    rb3 = new JRadioButton("BSc");
    rb3.setBounds(130, 130, 100, 30);
    rb4 = new JRadioButton("BCA");
    rb4.setBounds(180, 130, 100, 30);
    chb1 = new JCheckBox("Please verify the deails!!");
    chb1.setBounds(30, 150, 200, 50);
    ButtonGroup bg = new ButtonGroup();
    bg.add(rb1);
    bg.add(rb2);
    bg.add(rb3);
    bg.add(rb4);
    b = new JButton("Submit");
    b.setBounds(100, 200, 80, 30);
    b.addActionListener(this);
    add(l1);
    add(l2);
    add(l3);
    add(l4);
    add(rb1);
    add(rb2);
    add(rb3);
    add(rb4);
    add(b);
    add(chb1);
    add(t1);
    add(t2);
    add(t3);
    add(t4);
    setSize(300, 300);
    setLayout(null);
    setVisible(true);
  }

  public void actionPerformed(ActionEvent e) {
    if (chb1.isSelected()) {
      JOptionPane.showMessageDialog(this, "Registered Successfully");
    } else {
      JOptionPane.showMessageDialog(this, "Please verify the details!!");
    }
  }

  public static void main(String args[]) {
    new Registeraion();
  }
}
