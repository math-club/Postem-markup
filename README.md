# Postem

**Postem** is a work in progress lightweight **markup language** focused on speed of writing.

## Syntax description

### Basics

#### Text

```bnf
text ::= <Any unicode characters>
```

#### Numeric

```bnf
num ::= "0".."9"
```

### Alias

```bnf
text "." "=" text
```
#### Century alias

```bnf
century_alias ::= "_"numeric"e"
```

#### Line alias

```bnf
line_alias ::= "_"numeric<any ASCII character except "e">
```

#### Date alias

```bnf
date_alias ::= "_date"
```

### Text formatting

#### Title

```bnf
title ::= '&' .. '&&&&&&' text
```

#### Conclusion

```bnf
".." text
```
#### Simple definition

```bnf
text "::" text
```

#### Complex definition

```bnf
text "::" text ["*" text]*
```

#### Text block

```bnf
text "%" text ["%" text]*
```

## License

Distributed under the **GPL-2.0 License** . See [license](LICENSE) for more information.