Const PARMFLAG_CONST As Integer = &H1
Const PARMFLAG_CONV_MAJORITY As Integer = &H4000
 
Private Sub MyRoutine
 
  Dim oFoo As IDLexFoo
   
  Dim parmStr As String
  Dim parmVal As Long
  Dim parmArr(1, 2) As Long
   
  Dim argc As Long
  Dim argv(2) As Variant
  Dim argpal(2) As Long
   
  parmStr = "I am a string parameter"
  parmVal = 24
  parmArr(0, 0) = 10: parmArr(0, 1) = 11: parmArr(0, 2) = 12
  parmArr(1, 0) = 20: parmArr(1, 1) = 21: parmArr(1, 2) = 22
   
  argc = 3
  argv(0) = parmStr: argpal(0) = PARMFLAG_CONST
  argv(1) = parmVal: argpal(1) = PARMFLAG_CONST
  argv(2) = parmArr: argpal(2) = PARMFLAG_CONST + _PARMFLAG_CONV_MAJORITY
   
  Set oFoo = New IDLexFoo
   
  On Error GoTo ErrorHandler
   
  oFoo.CreateObject argc, argv, argpal
   
  ' use object here...
   
  Return
   
  ErrorHandler:
  If Not oFoo Is Nothing Then
  Debug.Print oFoo.GetLastError
  End If
 
End Sub