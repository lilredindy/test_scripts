//
//  FirstViewController.h
//  TestAutomation
//
//  Created by Jean-Christophe Amiel on 1/9/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface FirstViewController : UIViewController<UITextFieldDelegate>

//@property (nonatomic, copy) NSString *someText;
@property (nonatomic, strong) IBOutlet UILabel *displayText;

//@property IBOutlet UITextField *textField1;
//@property IBOutlet UITextField *textField2;

@end
