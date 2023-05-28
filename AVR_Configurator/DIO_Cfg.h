/***************************************************************************/
/*                           AVR CONFIGURATOR                              */
/*          Author: MOAZ OMAR                                              */
/*          EMBEDDED SOFTWARE ENGINEER @ ITI-INTAKE 43                     */
/*          DATE:  25/01/2023 23:11:48                                     */
/***************************************************************************/




#ifndef_DIO_CFG_H
#define_DIO_CFG_H


/***************************************************************************/
/* PORTA                                                                   */
/***************************************************************************/


#define DIO_PORTA_PIN0_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTA_PIN1_MODE     DIO_OUTPUT_LOW
#define DIO_PORTA_PIN2_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTA_PIN3_MODE     DIO_OUTPUT_LOW
#define DIO_PORTA_PIN4_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTA_PIN5_MODE     DIO_OUTPUT_LOW
#define DIO_PORTA_PIN6_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTA_PIN7_MODE     DIO_OUTPUT_LOW

/***************************************************************************/
/* PORTB                                                                   */
/***************************************************************************/

#define DIO_PORTB_PIN0_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTB_PIN1_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTB_PIN2_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTB_PIN3_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTB_PIN4_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTB_PIN5_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTB_PIN6_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTB_PIN7_MODE    DIO_INPUT_HIGH_IMPEDANCE

/***************************************************************************/
/* PORTC                                                                   */
/***************************************************************************/

#define DIO_PORTC_PIN0_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTC_PIN1_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTC_PIN2_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTC_PIN3_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTC_PIN4_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTC_PIN5_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTC_PIN6_MODE     DIO_INPUT_HIGH_IMPEDANCE
#define DIO_PORTC_PIN7_MODE     DIO_INPUT_PULL_UP

/***************************************************************************/
/* PORTD                                                                   */
/***************************************************************************/

#define DIO_PORTD_PIN0_MODE     DIO_OUTPUT_LOW
#define DIO_PORTD_PIN1_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTD_PIN2_MODE     DIO_OUTPUT_LOW
#define DIO_PORTD_PIN3_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTD_PIN4_MODE     DIO_OUTPUT_LOW
#define DIO_PORTD_PIN5_MODE     DIO_INPUT_PULL_UP
#define DIO_PORTD_PIN6_MODE     DIO_OUTPUT_LOW
#define DIO_PORTD_PIN7_MODE     DIO_INPUT_PULL_UP


/***************************************************************************/
/*             END OF CONFIGURATION XD                                     */
/***************************************************************************/


#endef _DIO_CFG_H
