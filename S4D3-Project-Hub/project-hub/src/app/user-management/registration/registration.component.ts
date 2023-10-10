import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RegistrationService } from './registration.service';
import { HttpClient } from '@angular/common/http';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  // registrationForm !: FormGroup;

  successMessage: string | null = null;
  failureMessage: string | null = null;


  user = {
    name: '',
    email: '',
    password: '',
    address:'',
    role:'',
    profile_picture:''
  };

  // constructor(
  //   private formBuilder: FormBuilder,
  //   private registrationService: RegistrationService
  // ) {
  //   this.registrationForm = this.formBuilder.group({
  //     name: ['', Validators.required],
  //     email: ['', [Validators.required, Validators.email]],
  //     password: ['', [Validators.required, Validators.minLength(6)]],
  //     // Add other registration fields here
  //   });
  // }

  constructor(
    private http: HttpClient,
    private toastr : ToastrService,
    private router : Router,
    ) {}


  onSubmit(): void {
   const registrationData = {
    name : this.user.name,
    email:this.user.email,
    password:this.user.password,
    role:this.user.role,
    profile_picture:this.user.profile_picture
   }
   this.http.post(
    'http://localhost:8080/projecthub/register' , 
    registrationData
   )
   .subscribe(
    (response) => {
      // this.successMessage = 'Registration Successfull!';
      // this.failureMessage = null;
      Swal.fire('Congratulations', 'You have Successfully registered. Now You can Login... ', 'success');

      console.log('Registration Successfull',response);

      setTimeout(()=>{
        this.router.navigate(['/dashboard']);
      },2000);

    },
    (error)=>{
      // this.failureMessage = 'Registration Failed';
      // this.toastr.error('Registration failed. Please try again.', 'Error', { timeOut: 3000 }); // Show error toast
      // this.successMessage = null;


      Swal.fire('Oops...', 'Registration Failed. PLease Submit the Details Again to Register... ', 'error');
      console.log('Registration Failed: ', error)
    }
   )

  }
}
